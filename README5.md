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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c15777f1-70b0-342b-84f0-4d8b46119686 | -10.48634 | -51.63192 | 2025-08-31 00:30:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8b33b8ba-e432-38ee-824c-305e121babb6 | -11.29052 | -43.58689 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 89c66948-e2a3-3dde-9eac-a00405c44ae1 | -7.86086 | -46.96416 | 2025-08-31 00:30:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5b7c1df7-7d21-353b-8ecf-c230f1800725 | -11.2988 | -43.57352 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 815ebd99-fab4-3ebb-9f38-4675049a108c | -8.95718 | -50.00838 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cb3b76b0-c7dc-371e-b5ff-6fb501b70858 | -8.8925 | -45.09615 | 2025-08-31 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| c1fc9ca0-e847-3986-bcc8-74bd50bf8a9d | -10.9399 | -50.82742 | 2025-08-31 00:30:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 37b8e28e-6afe-3c01-942f-f10985b3cb09 | -8.50038 | -44.737 | 2025-08-31 00:30:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eb12ca94-b438-3a9f-af1e-b30c69bfbea3 | -8.71857 | -50.36472 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 4d0382bc-95bb-3203-b964-508821e417c2 | -7.58887 | -42.70759 | 2025-08-31 00:30:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| ba2cd5ff-5fd7-3fa4-a20e-bab98f4bee25 | -8.8478 | -45.73448 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 76a7496e-9925-3ec0-a378-89ef2210ee47 | -8.92265 | -40.44258 | 2025-08-31 00:30:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 17.1 |
| bfa7567d-5f63-321f-be73-ef3124bed345 | -10.60457 | -44.33454 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c70b2500-20ad-3466-9c28-9ac2c281cdd4 | -10.60738 | -44.90626 | 2025-08-31 00:30:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c3308fd3-abfa-3f93-8f49-8068895e8384 | -12.92472 | -56.97157 | 2025-08-31 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0b1f5add-ee3d-3f2d-befa-8f57152e205f | -8.29505 | -46.32154 | 2025-08-31 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dc3ee165-2d2a-31e4-aaef-2c41a99c1487 | -10.02609 | -48.37139 | 2025-08-31 00:30:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dc353648-6891-375b-88a7-ac9c6d000e70 | -8.96954 | -50.0281 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d5b377cb-689e-3eee-9879-e3db3e00d3b2 | -13.02636 | -56.91586 | 2025-08-31 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| a87350a0-16f0-3f73-9624-379c77e757a9 | -11.56243 | -47.61452 | 2025-08-31 00:30:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5635435a-bb96-3d9c-8bf8-9b419fbd2ab2 | -11.83296 | -51.49796 | 2025-08-31 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 88c02d0a-7339-37f6-acf2-fe3205cd8485 | -11.29702 | -43.56152 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2fb71f4e-870d-397c-8b12-2e0996de40bd | -10.96382 | -50.84992 | 2025-08-31 00:30:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3a8b2f31-365b-3acf-a7ab-a08b4d311b63 | -9.58888 | -54.48156 | 2025-08-31 00:30:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 1fb0562f-68fa-388f-befd-5e63a17d07ed | -11.3028 | -43.66901 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 33ba856f-c567-3ac8-bfb7-165dc95a5890 | -11.20945 | -45.0435 | 2025-08-31 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5fabf6d2-87ce-3990-a7e8-8ecadeeba7a3 | -11.41451 | -44.68575 | 2025-08-31 00:30:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 177368ba-6089-3a7c-926f-00592954479e | -8.88305 | -45.09761 | 2025-08-31 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| cf03142c-0411-3fbe-bb3a-13224abab9a7 | -11.32448 | -43.67739 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a03f9772-6035-34d7-b483-98eda1a8ed6d | -11.06606 | -52.04641 | 2025-08-31 00:30:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 087fc616-fa68-333f-856e-15ad21b9bca5 | -10.94389 | -50.83265 | 2025-08-31 00:30:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b8d41433-d5bd-3ffc-96a1-39dac9c017b9 | -10.2411 | -50.85411 | 2025-08-31 00:30:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 501aec96-dabb-3aa9-92ce-3adc65997ebd | -8.88151 | -45.08717 | 2025-08-31 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 88d477ed-c8ac-3bfc-a6a6-7659d9520b11 | -11.84494 | -51.49018 | 2025-08-31 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1302eebd-7b11-390e-ab27-ca111f72e393 | -11.05801 | -44.63943 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4ca92d8a-42c8-3728-b458-24af30adcab8 | -8.19565 | -42.32055 | 2025-08-31 00:30:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 45ee1ee0-b2f9-34a8-be13-a5e78689b993 | -9.47117 | -47.61516 | 2025-08-31 00:30:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 534e8ecf-ff93-3a57-af5b-845235619c53 | -11.56367 | -47.62361 | 2025-08-31 00:30:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 07db96fd-4d40-3e0f-8131-653b5957e186 | -11.0754 | -44.6262 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c1c194fc-f876-3e8f-861d-3cf6c09f25c9 | -10.60068 | -44.32993 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 48603a37-0ac9-39a6-8f70-2a1d3e8b19bc | -9.25733 | -47.06218 | 2025-08-31 00:30:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 655e3401-3696-3469-97bb-5b68cb6f2348 | -8.04746 | -46.91568 | 2025-08-31 00:30:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6639877d-a14d-35f6-ae28-d4a936634277 | -11.84218 | -51.482 | 2025-08-31 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bd1aed82-a0f9-3ef0-a58c-3441b8878727 | -11.06746 | -44.63797 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7698d8a6-0d0b-398c-b45d-b27350a9ddc6 | -9.46994 | -47.60625 | 2025-08-31 00:30:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 425ec8cb-19b2-3339-a176-06d4a38fb932 | -7.63894 | -42.66242 | 2025-08-31 00:30:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| c79e7f6a-11bd-33ee-9ce8-873fed81fcd3 | -9.95822 | -46.35123 | 2025-08-31 00:30:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a169b1eb-38ca-3068-9e98-bed0e52234da | -10.20195 | -55.44462 | 2025-08-31 00:30:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 8981263f-1365-3ece-b792-89beb2f1559f | -7.37071 | -43.40248 | 2025-08-31 00:30:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0d8abaca-8d97-3806-a7e8-04a584e5464c | -10.23953 | -50.84179 | 2025-08-31 00:30:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 71423874-bd89-31a9-b059-9b74b522fdcb | -11.28928 | -43.64706 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e0b3b8b7-3154-3376-b5cc-3d7957d3c0f0 | -10.95028 | -50.82605 | 2025-08-31 00:30:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| e87decea-9b58-3f03-89eb-7eb5f7d4be2f | -10.20199 | -55.4497 | 2025-08-31 00:30:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| da5524e5-8933-3921-8727-24da398765d8 | -8.54425 | -45.80728 | 2025-08-31 00:30:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cc090c0f-da4b-3b0f-98f6-de205e586d22 | -8.96674 | -50.00708 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8fa8c541-11a8-39a0-975e-4569e8341fc0 | -9.6959 | -47.04688 | 2025-08-31 00:30:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c8969fe2-755c-3186-8065-2a5242c6bbbd | -7.59117 | -42.72309 | 2025-08-31 00:30:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 13a85714-10e4-36e5-a497-bc38512fe683 | -10.96223 | -50.83728 | 2025-08-31 00:30:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ce276c00-d5e4-3c33-aa25-81b94a9ef95e | -8.03681 | -45.42044 | 2025-08-31 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a607ba1f-738b-3505-b914-e7a5e90b54a4 | -9.74727 | -47.14252 | 2025-08-31 00:30:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 100ceb1f-5912-3339-8235-620592f6d402 | -10.5991 | -44.31908 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 118260bd-eeb6-3137-9911-9be988f55c42 | -9.66314 | -48.34361 | 2025-08-31 00:30:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 21739a40-4eeb-37a2-adb1-138fa0fb3871 | -8.71714 | -50.35379 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 20895882-798e-369d-892a-4370dd1c82c3 | -11.84668 | -51.5048 | 2025-08-31 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| bb5eb0ca-fbf4-38b8-ac94-b1051021131f | -10.94224 | -50.82007 | 2025-08-31 00:30:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f4b8bb57-a09c-3663-8878-7b2e7ce8afb0 | -11.2928 | -43.67051 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6f5633ab-e8b6-31fd-b850-e284e0a5829f | -6.96446 | -44.31829 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f2e1caa0-1a1d-3226-96dc-906363521247 | -6.18321 | -43.31461 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7cdb1af3-b122-30fa-9c71-fcb7946631c3 | -7.75312 | -47.44641 | 2025-08-31 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f5950e91-d15a-3178-8127-62b2605269dd | -4.42022 | -47.61345 | 2025-08-31 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46494303-46b0-3fd6-80cb-f25d45fbf79d | -3.58811 | -47.52978 | 2025-08-31 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9dac8293-c6ec-3ef9-a405-81a8236202c4 | -3.84307 | -49.29206 | 2025-08-31 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81fc418a-9b52-3a38-ab5a-877d860433b3 | -7.44801 | -44.81631 | 2025-08-31 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| acc1649f-d2c9-36c5-90c7-c83e2b7f8746 | -3.81449 | -48.9527 | 2025-08-31 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 29d07cae-369c-37d0-aa68-8c1b0a43c5f8 | -6.71345 | -51.4244 | 2025-08-31 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ffb3df04-b633-3411-a825-43158d29db5a | -7.24159 | -45.45839 | 2025-08-31 00:33:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c7eeb5b6-1b37-393e-b1ab-82e6912976bc | -5.73829 | -44.12178 | 2025-08-31 00:33:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 54a61499-1cec-33e7-8320-a638aad4bd7c | -7.71868 | -50.3033 | 2025-08-31 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 64bf7966-cf4a-35ea-8d9c-7d59e6069f7b | -4.26726 | -48.63449 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b7a0700f-0ffe-3e21-9334-91d14af941a2 | -7.09976 | -44.32812 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 97d49ffc-5c37-36d2-ae58-a94a747e5622 | -4.15679 | -46.78568 | 2025-08-31 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 283d3ca9-68b2-38b6-ae71-49344b3f996c | -5.48035 | -51.21861 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3ba2cf96-93d6-3fcc-bc2e-e6f0aeccb926 | -4.2773 | -48.64204 | 2025-08-31 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ceff09a4-dd2c-3b2c-9453-20cf9518c90c | -3.85195 | -49.29083 | 2025-08-31 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| befe828c-8a70-3976-9c95-ef626c4be84b | -7.45776 | -49.59378 | 2025-08-31 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 7ab63ee2-af4c-32c4-9160-07e13ea51b67 | -5.48262 | -51.22384 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 2597b735-06f8-3dda-8da3-ddd70ab62d83 | -5.99995 | -44.72421 | 2025-08-31 00:33:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 708a06dd-66de-3124-9bc9-301d1cea7349 | -4.65257 | -46.38252 | 2025-08-31 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b4f35b40-2d0e-3b75-b467-a95e9b310510 | -4.73988 | -44.44294 | 2025-08-31 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| ec2b9a74-f555-3af9-bb12-b086a054203b | -3.58685 | -47.52074 | 2025-08-31 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| b24eefc8-3658-3c5c-a19a-22f27cb119c4 | -6.57393 | -43.69137 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 066c73bf-26fc-3631-b45a-54d8d2147d43 | -3.5972 | -47.52224 | 2025-08-31 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6c6acd41-a3a8-3e53-9b73-cf8c382ced54 | -5.73639 | -44.10874 | 2025-08-31 00:33:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fb196407-71bf-3112-b94a-2ed31a45eb60 | -4.65398 | -46.39242 | 2025-08-31 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4b974781-c403-36be-a8e3-b2cfd60564f2 | -7.4001 | -49.51342 | 2025-08-31 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1bfb23e3-796f-3f9d-911e-5d32ca01efab | -6.62475 | -43.73817 | 2025-08-31 00:33:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9430b3b0-defe-3d15-aaad-ddc11408cdc6 | -6.95244 | -44.30754 | 2025-08-31 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a63ce870-1d38-3720-b006-5335553a8b5a | -2.76955 | -49.19933 | 2025-08-31 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 62e32bb9-4733-332f-a6bc-56c5fc028924 | -6.34025 | -53.43122 | 2025-08-31 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| bf783bb6-1b30-3a60-ae2e-2b0096187915 | -2.27032 | -47.85716 | 2025-08-31 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |


[Clique aqui para ver as próximas entradas](README6.md)
