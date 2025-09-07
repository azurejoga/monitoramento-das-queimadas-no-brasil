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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fab6643-14e6-36c1-9698-53e4c9d59b34 | -17.38327 | -49.23656 | 2025-09-07 05:14:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5780b08e-a2ee-3c48-b325-be42fe903303 | -14.93243 | -55.89612 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d1156a0-7381-3e49-ae2a-2e30f1cd2bd2 | -15.17765 | -47.97399 | 2025-09-07 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8da0c301-3d4f-35d3-95a7-e7fdd9247ba8 | -14.58438 | -48.10439 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74c11779-1a36-3f31-ab55-66346516d5cd | -18.0761 | -47.98925 | 2025-09-07 05:14:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7b17dc6-e746-3d21-8ca1-7373099a2b44 | -12.41759 | -63.89516 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bab950e-c64d-397c-974a-ce6ee32a7979 | -14.50462 | -48.7684 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a12e51a-5652-3174-b700-e114f1258844 | -14.56436 | -49.13046 | 2025-09-07 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1d3fb96-4ab1-3649-b78c-ff5cbc5d5efb | -14.93234 | -55.89366 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09ac01f6-afd2-31a3-bcf4-97bf9066cc3f | -12.41636 | -63.90218 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea823853-10b1-3ab9-a1f6-b6d7276ee8f8 | -16.68827 | -46.80301 | 2025-09-07 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5ad0ae23-4f88-3458-b52d-d17ce8feec0a | -18.73299 | -49.6296 | 2025-09-07 05:14:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9ea7ed9b-3812-3e6e-b021-73a1b674311d | -19.87786 | -57.89162 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.2 |
| c82c0ae5-40a4-3020-97b9-5614ffbeeb58 | -15.53474 | -48.37638 | 2025-09-07 05:14:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bcff944-4507-3e2f-8420-f1395d7d5840 | -16.28555 | -45.67856 | 2025-09-07 05:14:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16dd0743-4082-30dc-b9c7-37fc1c1be77f | -13.93923 | -54.02985 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28faec1e-fe4f-3a5e-91d1-036c1dafccfa | -19.87082 | -57.8905 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 3fd7dcb3-7c7d-35a7-8165-6421052e7d2d | -19.88785 | -57.89747 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8a77e5d8-cbd4-349f-b266-55e675ed9b2b | -20.82662 | -49.43063 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 22f691e2-ee16-3620-9457-a0a47d519da3 | -15.50111 | -52.77504 | 2025-09-07 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fe955bb-31b4-38b7-b0c7-0f91acf10e1c | -15.0731 | -50.07821 | 2025-09-07 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 383c019f-986c-3af6-a0fc-909b59c9da7f | -14.78222 | -48.1202 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d25c1c00-59d8-3cb6-a69e-bcf70fd933b1 | -13.80681 | -56.60415 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efa85679-1f0b-3ad5-900b-1ea264d0ae2b | -16.9371 | -45.7617 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8c54b4e-5058-35e3-9fca-897ad41c3454 | -14.93601 | -55.89425 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd99a868-74c8-3f90-99ad-f9d5805cf561 | -15.38544 | -52.91409 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47837431-bcd4-3f4a-8066-aa4d4efa11aa | -14.42062 | -60.19168 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 09666022-6a6a-3c45-9b1e-73b4a9668b47 | -13.91667 | -53.98196 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 615e3799-5469-3c04-8225-1d0fca58c82d | -19.06629 | -46.77697 | 2025-09-07 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3d280388-3bcc-32ba-b74d-088447528e8b | -12.42555 | -63.8966 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 043c06d9-9563-33d3-91f0-164af79289e0 | -19.87376 | -57.89524 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 42b17891-f101-3879-a523-6b89b6b616dc | -14.8517 | -46.69308 | 2025-09-07 05:14:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fc6fa390-b7b6-3821-bed8-c7b25bc2e2dd | -14.93847 | -55.82149 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a0be40-b7c7-39aa-8afd-9a0491d4c0bd | -12.41698 | -63.89867 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2476ed1b-67ae-3818-ad3d-a267f0765431 | -14.49924 | -53.25108 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63940d9b-642d-328c-88ee-2c782f72a5d7 | -14.77663 | -48.11515 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e721192-91e1-3498-ab6a-62e846a52bdf | -14.89043 | -55.82137 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 714825d6-2b10-35c8-bf61-c923c61d6fcf | -13.89388 | -53.99424 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6eeb7be-3359-3cad-84bf-db96dbca3dc5 | -15.7068 | -53.5657 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa600782-036c-32c4-8bcd-3930c31812d2 | -14.42669 | -60.19641 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4ba57e3-3198-3eae-a205-f3d3c325e08e | -14.92813 | -55.89995 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c667347c-1bae-3d9d-97b3-cf769ca39ee4 | -20.5385 | -46.44432 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9d1e3ade-4a9f-35b9-b079-ede7bfee77a2 | -20.53465 | -46.4406 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2123627d-94f1-3417-b5d7-d0e5fc01422c | -19.06561 | -46.7785 | 2025-09-07 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4c678fa6-60ca-352b-856b-32ad2bc00a41 | -13.89804 | -53.99777 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b19b2c24-8884-351a-a13e-f681901c7a5b | -13.90661 | -53.99548 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 786ae59f-c25d-31b0-92a5-898b422419c4 | -14.35103 | -60.33048 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1939f1f4-06e6-30f7-84de-ab3dd1c7ad38 | -14.57712 | -49.11936 | 2025-09-07 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72c2d77c-ac34-328d-9688-9b30a1cf5e68 | -14.45588 | -48.45336 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d53debd-b564-3e15-8ab4-3ca2034c7e53 | -13.92071 | -53.98267 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cfcf3b7-84ba-3356-90da-76408d21ad5c | -14.8533 | -46.69697 | 2025-09-07 05:14:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f426d5f9-5749-302a-bc9f-9887a39d4bf7 | -14.58965 | -52.14505 | 2025-09-07 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8758aa7b-0207-3b2b-8d02-cc8fc665fbd6 | -13.82423 | -56.07752 | 2025-09-07 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33157d9a-8d28-3756-a8a9-7d69560e8e00 | -20.83343 | -49.42242 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 44284e9e-b20f-3073-a2ac-82918f712702 | -14.41623 | -49.68586 | 2025-09-07 05:14:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 023c51c6-1728-39d9-aea7-8f98ef992499 | -15.12416 | -52.35117 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 194224f7-6ae3-30a7-8419-5a7c9822e83f | -16.82277 | -49.18931 | 2025-09-07 05:14:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0010e79-0c50-3134-97e3-a6d6582341a2 | -13.89853 | -53.99398 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1294254e-71ba-3412-8546-7e68de32aedc | -13.90612 | -53.99921 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69c0e411-df31-3eab-b0c0-dbfe97345262 | -14.5942 | -48.08599 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10a2287a-4673-3635-a643-201df7d3403a | -15.37296 | -46.42238 | 2025-09-07 05:14:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32d5f773-4e27-37be-ab3e-058fbd6e9bb4 | -19.07201 | -46.78466 | 2025-09-07 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 18d3bdd9-53f2-39a8-a448-4941acec17c2 | -20.5457 | -46.44338 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb5b4c5c-119d-3a08-9e25-aa8b51861bf5 | -15.57496 | -52.89948 | 2025-09-07 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13e307bd-415f-30fe-81a6-33d864a135ef | -13.93971 | -54.02628 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c720ee1-b95a-316b-870e-4e5397fe45fe | -14.44924 | -48.45972 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4c3c85b-3710-3332-a6ed-a9a16862921d | -14.60071 | -48.08244 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c31f613-f7a9-3792-96ed-6648217085ad | -16.28679 | -58.12172 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c999a0e5-eb9d-31ae-afaa-5862207d7af8 | -13.90516 | -54.00653 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4e38b4c-7c23-314a-869f-b2d3066db435 | -14.57885 | -48.09893 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 639fa8e5-4e4c-35da-ba89-2e912834e3e0 | -14.90861 | -59.53815 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f90959e-6c41-38ab-bc4c-ab8f8e85ca8b | -13.91571 | -53.98922 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75494960-9479-376b-a69b-128fb81281c1 | -15.71108 | -47.51051 | 2025-09-07 05:14:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4b20c38-9cbe-3835-b5bf-476f42bf90e4 | -17.40546 | -49.3077 | 2025-09-07 05:14:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe30cfe0-3813-3ebd-a108-0a9e6ce73797 | -15.01247 | -48.00523 | 2025-09-07 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c50c8e6-0bd4-319d-a971-97e24625c534 | -16.29207 | -45.68643 | 2025-09-07 05:14:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43d1ff53-aa8e-38ff-906f-91cb85e9ec40 | -16.29413 | -58.119 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2f35ebc2-84a4-3664-a1d7-5ba555048f69 | -16.33256 | -58.11731 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a90cd840-775a-390c-8930-7a9e7831a711 | -13.90564 | -54.0029 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4560ed3c-3362-31e8-b766-7aa43673bd31 | -14.4873 | -48.76558 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b55d19ce-52fd-335f-9a23-ab695661aceb | -19.07271 | -46.78319 | 2025-09-07 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0156708a-9ea0-37ce-b3e9-e25cb66a8507 | -15.69878 | -53.56018 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f962515-4699-3e7c-b835-9a587d282fad | -20.8299 | -49.42665 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| acbd0628-ca34-3a0d-b7e3-82be666f740c | -14.42005 | -60.19528 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4743a1d8-8c68-36e8-80f8-c523b5667cb4 | -16.28735 | -58.11795 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a6bacf73-b64f-35a0-bd7f-ddb9353dea2b | -19.07252 | -46.77877 | 2025-09-07 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8c35e9ac-9a69-3930-adb9-d5152a900a3d | -15.84395 | -52.27289 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de15fbbc-43d9-33cf-bc0e-0b8ad0288a1f | -20.82704 | -49.42615 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| efe57490-64c1-3a8b-8199-81a88f0d198c | -12.42095 | -63.89939 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b6b03d0-5904-3ec2-9ea2-50b45da6c86e | -19.87024 | -57.89468 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| b5d5abf0-33b1-3309-95f4-5ccf9140fba3 | -20.53132 | -46.44485 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 117daf13-d41b-3ca8-86f7-1407a96d6935 | -16.94428 | -45.76189 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cf6a2dfb-35aa-376d-b19f-ee356f85c033 | -12.84452 | -62.03727 | 2025-09-07 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9c59cc7-bcb1-3aab-91d6-cdd4dd32389f | -20.53414 | -46.44721 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8f353a43-70ec-32fe-8464-9f39e0bd895b | -14.59229 | -48.10449 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c13262c7-d7e7-39a5-94c1-730533ef80c9 | -14.49837 | -48.77165 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0a6f3d6-fe4f-3499-8c6d-58132d0ad42d | -14.58893 | -48.07763 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d2f9258-d6ea-33d7-8aa2-97c6388154f7 | -15.338 | -52.74519 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0327d043-9129-346e-a18c-01808924fff8 | -15.18378 | -47.97486 | 2025-09-07 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 92493a5c-8d52-3d27-bd02-8018c0b6e18a | -14.82022 | -48.18348 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README75.md)
