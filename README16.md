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
| d42efe15-add7-3a62-9686-ecc0f2e0fbcf | -11.1002 | -49.9151 | 2026-08-18 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb20c05d-9006-3c77-81ce-679db560808e | -14.81396 | -46.63681 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 28d7c290-573d-3b59-9142-2a63f6f13711 | -14.87508 | -46.63398 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2e4fb76-dbd2-3b96-af7b-09ac84118936 | -12.769 | -48.4315 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06f4ee90-8617-35b6-ae64-acd023c12c27 | -14.8431 | -46.63309 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 487887d3-a314-3ce5-95e7-f0bb015cbbb9 | -13.79096 | -53.84918 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fac8d652-3dd3-3915-b333-ad415eba30e2 | -14.26306 | -51.93732 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae967618-5d39-34ff-914d-6c86857ee750 | -14.25431 | -51.92375 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3db500f-05b1-3be5-b35e-02c7154c2e1b | -11.13738 | -47.28191 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ec8291d-f8c6-3640-a503-bc4fc142e7f6 | -14.16434 | -52.91607 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 627e7024-4736-30e3-9761-2cef4447d144 | -11.12526 | -46.49619 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 648c845c-a67d-3027-86d8-07e6a25bf239 | -13.93391 | -53.93215 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36aee0a5-8619-3239-8e6a-1bf8d1eca764 | -11.10137 | -49.90885 | 2026-08-18 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3da0984d-4c4b-3d6b-91bc-1073f5a835f1 | -16.86709 | -44.2732 | 2026-08-18 04:04:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d159789-1ad4-39b2-89dc-e4f10b7d8a85 | -14.17692 | -52.91458 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb1b4444-6512-3405-a546-211d483e0730 | -13.58113 | -51.78254 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6dc0f030-61fe-39e6-a54c-092ac2657798 | -17.10836 | -46.57584 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e579f36-dc89-3bd0-aa46-9da8e1de62e5 | -13.9378 | -53.92956 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 652b27bb-b166-386d-9419-e0e72fa11c13 | -11.13224 | -47.28578 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8fb2a16-b720-3763-8895-54ba9913a613 | -20.30776 | -46.47717 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da400c78-d5cb-3086-b5ea-a6a914daed1a | -20.46246 | -46.47047 | 2026-08-18 04:06:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b41f480-d34b-3d78-a255-549f57ab80db | -18.81426 | -46.75234 | 2026-08-18 04:06:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5351bc2b-830e-3423-81df-e94d37f93c41 | -23.18948 | -49.81123 | 2026-08-18 04:06:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 40bfd4b7-09f8-372a-8e6a-c3805ab8397b | -20.5998 | -45.93114 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 125b68d0-d6ac-3457-8dff-7050c5f7c432 | -20.31409 | -46.48317 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40d745d3-f491-327a-9551-e68a2ef8e5c6 | -20.6193 | -45.92236 | 2026-08-18 04:06:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dde0392d-bee6-32a4-b431-297495a19798 | -22.06226 | -55.9816 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9bb117da-1fef-351b-999c-84cbcfb6a728 | -18.9544 | -47.32452 | 2026-08-18 04:06:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89e0c376-c989-3c2f-beca-1e54a076c8c9 | -22.85258 | -42.89637 | 2026-08-18 04:06:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5a09c52c-d48c-33db-883a-e866a8c15d3d | -22.62764 | -46.23873 | 2026-08-18 04:06:00 | NOAA-21 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7c591b9f-b8b9-341a-9835-8f525a207f1c | -21.83498 | -45.43717 | 2026-08-18 04:06:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 21bca336-6109-3e8b-b670-9a9de5f6773a | -22.07348 | -55.98764 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 570266be-ea88-3540-822b-e5b135d8dea6 | -22.06142 | -55.9844 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 31e1a6d9-ca53-30c0-8539-b8d78593de20 | -20.30569 | -46.46798 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91e3e43e-e438-3b15-8a76-0864c8f4fca3 | -22.94423 | -46.67464 | 2026-08-18 04:06:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3e4ae870-fb6f-3c07-b053-de206474d880 | -22.06485 | -55.99719 | 2026-08-18 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d3db539-1062-3877-a48f-1079fc707b79 | -19.68651 | -49.03298 | 2026-08-18 04:06:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a61f1be0-0685-3bba-a8c3-0d4aa05af577 | -20.62276 | -45.92317 | 2026-08-18 04:06:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9e1bdd7-8f7a-3f0e-a01c-3ab347916f0b | -21.37242 | -46.71466 | 2026-08-18 04:06:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c4b116b-d20f-3aed-a861-b7e91f1e50d0 | -21.61738 | -49.01962 | 2026-08-18 04:06:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 746dbd5e-79b5-3317-bdb2-be64401e6c14 | -20.59902 | -45.93557 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c100ee2c-5842-3242-b42a-eccc67abd671 | -20.307 | -46.48147 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bf2e955b-e3c7-33a2-b504-08a2bf2851a1 | -23.53664 | -47.29911 | 2026-08-18 04:06:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b6e0143-b032-3bf5-8898-6835025c8b15 | -20.29785 | -46.47055 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f4c057bc-91cd-3996-afee-3f9c843217ae | -20.30421 | -46.47637 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0c1453fa-15c9-3ce2-b990-e55de1cec221 | -21.61809 | -49.0159 | 2026-08-18 04:06:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1760cc83-a9d0-361d-8981-968ff2112003 | -23.68119 | -51.68336 | 2026-08-18 04:06:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8a53a484-aab4-3322-a843-28fb8505309e | -20.84068 | -45.20177 | 2026-08-18 04:06:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c8c6f6c-1dd9-3650-a3cf-c263419fa322 | -21.72459 | -49.75698 | 2026-08-18 04:06:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 94398c7f-a117-300a-8207-7cabab3b6bf6 | -20.64249 | -57.91588 | 2026-08-18 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2de2f1bc-cff9-3886-8815-810f20887a08 | -23.38256 | -46.93716 | 2026-08-18 04:06:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e1ba4b9e-92ab-38ef-b0a6-289b4437b5d3 | -23.82359 | -48.70927 | 2026-08-18 04:06:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17e37245-0f70-3aff-bd06-5b05a5dd8457 | -18.9553 | -47.31958 | 2026-08-18 04:06:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79090f82-2db1-3ce8-8fb0-570bbd2af780 | -22.06692 | -55.98893 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7a6e4262-be5c-3fb0-b619-3730ff1015cc | -19.88668 | -44.07065 | 2026-08-18 04:06:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7bf698b7-90d9-327b-874c-4323ffae00a9 | -20.29854 | -46.46658 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e38d630a-ac39-34bb-97f4-f845ffa802d3 | -19.01842 | -47.05735 | 2026-08-18 04:06:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb04064d-b9bf-3cf6-af1d-43d82d1dfb31 | -20.62001 | -45.91827 | 2026-08-18 04:06:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a7d9dbd-7e7a-375b-acfb-d9eb381e7b7c | -20.29428 | -46.46981 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6e928e33-3ac5-3674-9df9-645cd61b9546 | -20.8498 | -49.35439 | 2026-08-18 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 33d0b9ef-ddb8-3b7d-a7e2-2f22d859d266 | -19.29712 | -46.50852 | 2026-08-18 04:06:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38a44b9e-bb41-3c63-b57a-377f799f2696 | -18.84712 | -47.14273 | 2026-08-18 04:06:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a66d0a5-795b-33ee-a595-b3c3ac723904 | -20.29633 | -46.45811 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e910d395-7eb3-3cee-a349-941053d25fa4 | -20.31335 | -46.48742 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61f909a1-89b0-3949-884a-7a3d3d0f0a43 | -23.8208 | -48.71086 | 2026-08-18 04:06:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12cbbc62-db0b-393f-baa7-7184ffa1ddca | -20.61242 | -45.92059 | 2026-08-18 04:06:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 596fb77d-ba98-301d-8c3a-c40ebbc6acd7 | -18.81506 | -46.74775 | 2026-08-18 04:06:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e2da05e-aafa-3900-b55d-81f2e8839eb5 | -22.06613 | -55.99169 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6ff715ee-aedf-3fa9-9ac6-351d09cffef3 | -22.07216 | -55.99332 | 2026-08-18 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74ab61a1-88c3-3d26-919d-51e4d84f5a28 | -22.83743 | -47.1173 | 2026-08-18 04:06:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4fe0121f-bd95-3abd-bbfd-1eb9db9d1eb2 | -22.06554 | -55.99468 | 2026-08-18 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1017b869-735f-3e99-ba1c-8e4692999ba0 | -21.98857 | -48.16312 | 2026-08-18 04:06:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d75eb48c-babe-3fb6-8be8-4b8dfa7a285e | -20.59665 | -45.92198 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7071326-6053-3cf5-bf27-542e724f7090 | -22.06281 | -55.97845 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bc623e8e-b51e-31ab-a909-328798f210c9 | -23.19197 | -49.15696 | 2026-08-18 04:06:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 782f0ae1-124c-3777-8401-e915dba09262 | -18.60268 | -48.20239 | 2026-08-18 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4504fe3b-a4e0-3000-acc8-20669f817c29 | -20.46323 | -46.46604 | 2026-08-18 04:06:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3a94456-65c2-3969-9eeb-0be177efadc8 | -20.30142 | -46.47125 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7bba183c-cfbc-3994-969f-ca7276581cd6 | -20.31132 | -46.47794 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82275d30-07f3-3a14-be2c-cd3c514a59dd | -20.59867 | -45.9313 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b212e3e1-c895-38ea-a42c-8ef9eab21b17 | -23.19047 | -49.15825 | 2026-08-18 04:06:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f6cade5-39e9-3434-8680-da8803528d0c | -20.59246 | -45.92548 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b95ee0e8-ebcc-38fa-9ae1-5c6dec81ff2a | -20.59792 | -45.93575 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 238e3d1e-f6ee-3e42-a9b0-872c39df9025 | -20.59174 | -45.92974 | 2026-08-18 04:06:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b54b5f54-7edf-3e9e-b99a-91a465e84d61 | -19.68727 | -49.02896 | 2026-08-18 04:06:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d0a8bc9-821e-3377-bd1c-94741136a7db | -20.30921 | -46.46894 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81d09f71-37fb-3f8f-9dc7-15dd343a0e94 | -23.68177 | -51.68058 | 2026-08-18 04:06:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b4325371-b982-392e-8dd4-e011f2d3fbef | -22.06828 | -55.98325 | 2026-08-18 04:06:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4a0b4ac1-911d-370c-9b71-143cf18d9bf8 | -20.31058 | -46.48218 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e7753433-105a-3a23-99cf-dd42ad0027f1 | -21.71959 | -49.76029 | 2026-08-18 04:06:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1b85bfd0-6cf4-3ddc-b6f6-f3fc8980b6e4 | -23.52119 | -47.2065 | 2026-08-18 04:06:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9f9bd60-58a1-39b6-8b09-9259577a4575 | -23.50735 | -50.91381 | 2026-08-18 04:06:00 | NOAA-21 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7aa14839-38d6-3837-8c1b-21edd72a7184 | -21.7204 | -49.75609 | 2026-08-18 04:06:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e2f71935-b63c-3dc1-afa2-0b16cc034e15 | -20.30065 | -46.4756 | 2026-08-18 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d0f9b9d-70dc-38fd-a312-ccba318939b7 | -19.86302 | -44.40844 | 2026-08-18 04:06:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bcc8a11-0193-3661-b0b0-4e2f911ad3aa | -19.91049 | -42.19141 | 2026-08-18 04:06:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c9d94262-89ad-381b-8a33-17c8e7323c45 | -19.23244 | -45.2888 | 2026-08-18 04:06:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d763243f-17a1-3270-8548-74d16838fe96 | -22.07158 | -55.99622 | 2026-08-18 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9b640403-e08d-3699-bfa3-d72b11fceb70 | -21.97529 | -48.17085 | 2026-08-18 04:06:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce6e5aa7-6141-38d8-9677-db9c77aa8e98 | -23.10014 | -49.16508 | 2026-08-18 04:06:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
